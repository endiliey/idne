import requests
import click
import time
from robobrowser import RoboBrowser

def get_latest_verdict(user):
    r = requests.get('http://codeforces.com/api/user.status?' +
                     'handle={}&from=1&count=1'.format(user))
    js = r.json()
    if 'status' not in js or js['status'] != 'OK':
        raise ConnectionError('Cannot connect to codeforces!')
    result = js['result'][0]
    id_ = result['id']
    verdict_ = result['verdict']
    time_ = result['timeConsumedMillis']
    memory_ = result['memoryConsumedBytes'] / 1000
    return id_, verdict_, time_, memory_

@click.command()
@click.argument('user_name')
@click.argument('passwd')
@click.argument('prob_id')
@click.argument('filepath')
def cli(user_name, passwd, prob_id, filepath):
    # get latest submission id, so when submitting should have not equal id
    last_id, b, c, d = get_latest_verdict(user_name)
    
    click.echo('Trying to login to codeforces')
    # Browse to Codeforces
    browser = RoboBrowser(parser = 'html.parser')
    browser.open('http://codeforces.com/enter')
        
    enter_form = browser.get_form('enterForm')
    enter_form['handle'] = user_name
    enter_form['password'] = passwd
    browser.submit_form(enter_form)
    
    try:
	    checks = list(map(lambda x: x.getText()[1:].strip(),
	        browser.select('div.caption.titled')))
	    if user_name not in checks:
	        click.secho('Login Failed.. Wrong password.', fg = 'red')
	        return
    except Exception as e:
	    click.secho('Login Failed.. Maybe wrong id/password.', fg = 'red')
	    return 
    
    click.secho('Successful Login, {0}'.format(user_name), fg = 'green')

    click.echo('Submitting problem {0} from {1}'.format(prob_id, filepath))
    browser.open('http://codeforces.com/problemset/submit')
    submit_form = browser.get_form(class_ = 'submit-form')
    submit_form['submittedProblemCode'] = prob_id
    submit_form['sourceFile'] = filepath
    browser.submit_form(submit_form)

    if browser.url[-6:] != 'status':
        click.secho('Failed submission, probably you have submit the same file before', fg = 'red')
        return

    click.echo('Successful submission, waiting for result ....')
    while True:
        id_, verdict_, time_, memory_ = get_latest_verdict('endijr')
        if id_ != last_id and verdict_ != 'TESTING':
            if verdict_ == 'OK':
                click.secho('OK', fg = 'green')
            elif verdict_ == 'WRONG_ANSWER':
                click.secho('WRONG_ANSWER', fg = 'red')
            click.echo('{} MS'.format(time_), '|', '{} KB'.format(memory_))
            break
        time.sleep(1)

if __name__ == '__main__':
    cli()