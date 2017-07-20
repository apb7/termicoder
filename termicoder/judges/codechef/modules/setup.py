"""
this module creates the required files of a contest/problem including
json data of contest(.contest file), json data of problem(.problem file)
html problem statements and testcases

for trial run run this as python3 setup.py
"""
from __future__ import print_function
import termicoder.judges.codechef.modules.utils.scrape as scrape
import os
import json

def setup_problem(problem_code,contest_code="PRACTICE"):
    problem_path=os.path.join(".",contest_code,problem_code)

    try:
        os.mkdir(problem_path)
    except:
        pass

    problem=scrape.get_problem(problem_code,contest_code)

    if problem["error"]==None:
        problem_html=problem.pop("body")
        sample_io=problem.pop("sample_io")
        # html problem statement
        if not problem["error"]:
            problem_html_path=os.path.join(problem_path,problem_code+".html")
            phfile=open(problem_html_path,"w")
            print(problem_html,file=phfile)     # TODO needs unicode fixture for python 2

        # sample_io files
        if(sample_io["error"]==""):
            testcases_path=os.path.join(problem_path,"testcases")
            try:
                os.mkdir(testcases_path)
            except:
                pass
            for i in range(len(sample_io["inputs"])):
                input_file=os.path.join(testcases_path,str(i+1)+".in")
                ifile=open(input_file,"w")
                print(sample_io["inputs"][i],file=ifile)
            for o in range(len(sample_io["outputs"])):
                output_file=os.path.join(testcases_path,str(o+1)+".out")
                ofile=open(output_file,"w")
                print(sample_io["outputs"][o],file=ofile)

    # the problem data
    problem_setup_file=os.path.join(problem_path,".problem")
    f1=open(problem_setup_file,"w")
    print(json.dumps(problem,indent=2,sort_keys=True),file=f1)


def setup_contest(contest_code):
    contest_path=os.path.join(".",contest_code)
    try:
        os.mkdir(contest_path)
    except:
        pass
    contest_setup_file=os.path.join(contest_path,".contest")
    f=open(contest_setup_file,"w")
    contest=scrape.get_contest(contest_code)
    if(contest["error"]==None):
        del contest["rules"]
    print(json.dumps(contest,indent=2), file=f)

    # setup all problems for the contests
    if(contest["error"]==None):
        for problem_code in contest["problems"]:
            setup_problem(problem_code,contest_code)

def login(status):
    print("setup login not implemented")

def logout(status):
    print("setup logout not implemented")
