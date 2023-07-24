from fabric import *

env.hosts = ['root@server2:22']
env.passwords = {'root@server2:22': 'root'}
env.roledefs = {
    'web': ['root@server1:22'],
    'db': ['root@server2:22'],
}


@roles("web")
def host_type():
    run('uname -s')


@roles("db")
def host_files():
    run('ls -al')


def all_files():
    run('ls -al')


@task
def go():
    all_files()
    # run('ls -al')


@task(default=True)
def who():
    run('whoami')


@task
@parallel(pool_size=2)
def para():
    run('ls -al')


@task
def argtest(arg1, arg2):
    print(arg1)
    print(arg2)


def test():
    return run('ls -al')


@task
def org():
    r = execute(test)
    print(r)


@runs_once
def db_init():
    print('db init')


@task
def deploy_db():
    db_init()
    db_init()


@task
def clean_and_upload():
    local('ls -al')
    put('fabfile.py', '/tmp/fabfile.py')
    with cd('/tmp'):
        run("pwd")
        run('ls -al')
        print(exists('/tmp/fabfile.py'))


@task
def color():
    print(green('success'))
    print(red('fail'))
