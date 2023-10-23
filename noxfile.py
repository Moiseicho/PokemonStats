import nox

@nox.session(python=['3.8'])
def tests(session):
    session.install('pytest', 'pytest-cov')
    session.run('pytest', '--cov=statsApp', '--cov=readerApp', '--cov=arena', '--cov-report=xml', '--cov-report=html')
    session.run('coverage', 'report', '-m')

@nox.session
def clean(session):
    session.run('rm', '-rf', '.coverage', 'htmlcov', 'coverage.xml')
