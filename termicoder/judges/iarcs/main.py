'''
this file first handles error/input with respet to this
judge and then forwards the request to correct module/function
'''

import click
import termicoder.utils.display as display
import termicoder.judges.iarcs.modules.view as view
import termicoder.judges.iarcs.modules.setup as setup_module
import termicoder.judges.iarcs.modules.utils.session as session

# try to load old session(if exists) before doing anything
session.load()

def view_contests():
    display.error("iarcs does not hold any contests")
    display.normal("you can view problems through:")
    display.command("termicoder view problems -j iarcs")


def view_problems(contest):
    try:
        assert(contest is None)
    except:
        display.error("unexpected input --contest for judge iarcs")
        display.normal("try:")
        display.command("termicoder view problems -j iarcs")
    else:
        view.problems()


def setup(contest, problem_code, status):
    try:
        assert(contest is None)
    except:
        display.error("unexpected input --contest for judge iarcs")
        display.normal("try:")
        display.command("termicoder view problems -j iarcs")
    else:
        if(status=="login"):
            setup_module.login()
        elif(status=="logout"):
            setup_module.logout()

        if(problem_code is not None):
            setup_module.problem(problem_code)
