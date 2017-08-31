import requests
import click
import time
from utils import config
from robobrowser import RoboBrowser

def safeget(dct, key):
    try:
        dct = dct[key]
    except KeyError:
        return None
    return dct

def get_latest_verdict(user):
    r = requests.get('http://codeforces.com/api/user.status?' +
                     'handle={}&from=1&count=1'.format(user))
    js = r.json()
    if 'status' not in js or js['status'] != 'OK':
        raise ConnectionError('Cannot connect to codeforces!')
    try:
        result = js['result'][0]
        id_ = result['id']
        verdict_ = safeget(result, 'verdict') 
        time_ = result['timeConsumedMillis']
        memory_ = result['memoryConsumedBytes'] / 1000
    except Exception as e:
        raise ConnectionError('Cannot get latest submission, error')
    return id_, verdict_, time_, memory_

@click.command()
@click.argument('prob_id')
@click.argument('filename')
def cli(prob_id, filename):
	# get latest submission id, so when submitting should have not equal id
    last_id, b, c, d = get_latest_verdict(config.username)
    
    # Browse to Codeforces
    browser = RoboBrowser(parser = 'html.parser')
    browser.open('http://codeforces.com/enter')
        
    enter_form = browser.get_form('enterForm')
    enter_form['handle'] = config.username
    enter_form['password'] = config.password
    browser.submit_form(enter_form)
    
    try:
	    checks = list(map(lambda x: x.getText()[1:].strip(),
	        browser.select('div.caption.titled')))
	    if config.username not in checks:
	        click.secho('Login Failed.. Wrong password.', fg = 'red')
	        return
    except Exception as e:
	    click.secho('Login Failed.. Maybe wrong id/password.', fg = 'red')
	    return 
    
    click.secho('[{0}] login successful! '.format(config.username), fg = 'green')
    click.secho('Submitting [{1}] for problem [{0}]'.format(prob_id, filename), fg = 'green')
    browser.open('http://codeforces.com/problemset/submit')
    submit_form = browser.get_form(class_ = 'submit-form')
    submit_form['submittedProblemCode'] = prob_id
    try:
        submit_form['sourceFile'] = filename
    except Exception as e:
        click.secho('File {0} not found in current directory'.format(filename))
        return
    browser.submit_form(submit_form)

    if browser.url[-6:] != 'status':
        click.secho('Failed submission, probably you have submit the same file before', fg = 'red')
        return

    click.secho('[{0}] submitted ...'.format(filename), fg = 'green')
    while True:
        id_, verdict_, time_, memory_ = get_latest_verdict('endijr')
        if id_ != last_id and verdict_ != 'TESTING' and verdict_ != None:
            if verdict_ == 'OK':
                click.secho('OK', fg = 'green')
            elif verdict_ == 'WRONG_ANSWER':
                click.secho('WRONG_ANSWER', fg = 'red')
            click.secho('{} MS | {} KB'.format(time_, memory_), fg = 'green')
            break
        time.sleep(0.5)

if __name__ == '__main__':
    cli()
