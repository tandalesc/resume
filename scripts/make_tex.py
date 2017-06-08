# Shishir Tandale

from argparse import ArgumentParser
import yaml

parser = ArgumentParser()
parser.add_argument("-input")
parser.add_argument("-out")
args = parser.parse_args()
in_file = args.input
out_file = args.out

#store lines of latex doc and tab information
class latex_data(object):
    def __init__(self, lst):
        self.tabs = 0
        self.list = lst
    def __call__(self, s=""):
        self.list.append("\t"*self.tabs + s)
#helper to manage indents and latex env wrapping
class latex_env(object):
    def __init__(self, env_name, latex, env_arg1=None, env_arg2=None, skip_ending=False):
        self.env_name = env_name; self.arg1 = env_arg1; self.arg2=env_arg2
        self.latex = latex; self.skip_ending = skip_ending
    def __enter__(self):
        latex_str = "\\begin{"+self.env_name+"}"
        if self.arg1 is not None: latex_str += "{"+self.arg1+"}"
        if self.arg2 is not None: latex_str += "["+self.arg2+"]"
        self.latex(latex_str)
        self.latex.tabs += 1
    def __exit__(self, exc_type, exc_value, traceback):
        self.latex.tabs -= 1
        if not self.skip_ending: self.latex("\\end{"+self.env_name+"}")
bold = lambda text: "\\textbf{"+text+"}"
section = lambda text: line("\section*{"+text+"}\n\\vspace*{-3mm}")

#parse attributes from yaml to latex lines and envs
with open(in_file, "r") as yaml_file:
    latex_buffer = []
    line = latex_data(latex_buffer)
    env = lambda e,arg1=None,arg2=None: latex_env(e, line, env_arg1=arg1, env_arg2=arg2)
    spec = yaml.load(yaml_file)


    line("\documentclass{article}")
    line("\\usepackage[utf8]{inputenc}")
    line("\\usepackage{multicol}")
    #line("\\usepackage{enumitem}")
    line("\\usepackage[top=0.6in, bottom=0.6in, left=0.6in, right=0.6in]{geometry}")
    line("\setlength{\columnsep}{10mm}")
    name = spec['header']['name']
    email = spec['header']['email']
    phone = spec['header']['phone']
    with env('document'):
        #line("\maketitle")
        with env('center'):
            line(f'\Huge {name} \par')
            line(f'\large {email} \hspace{"{2mm}"} {phone} \par')
        with env('multicols*',arg1='2'):
            #education
            section('Education')
            for school in spec['education']:
                line(' { \par ')
                with env('flushleft'):
                    line('\large ' + bold(school['name'])+ '\\newline \\normalsize')
                    line(school['degree'] + '\\newline')
                    line(school['date'])
                line('}')
            line('\\vspace*{-5mm}')
            #skills
            for skill_name, skill in spec['skills'].items():
                section(skill_name)
                with env('itemize'):
                    for cat_name, lst in skill.items():
                        line(' { \par')
                        line('\item \large '+bold(cat_name) + '\\newline \\normalsize')
                        line(", ".join(lst))
                        line(' } ')
                line('\\vspace*{-5mm}')
            #work
            section('Work Experience')
            for job in spec['work']:
                line(' { \par')
                with env('flushleft'):
                    line('\large ' + bold(job['name']) + '\\newline \\normalsize')
                    line(job['position'] + ' (' + job['location'] + ') \\newline')
                    line(job['date'])
                line('\\vspace*{-3mm}')
                with env('itemize'):#, arg2='nosep'):
                    for bullet in job['text']:
                        line('\\vspace*{-3mm}')
                        line('\item '+bullet)
                line(' } ')
            line('\\vspace*{-5mm}')
            #projects
            section('Projects')
            for project in spec['projects']:
                line(' { \par')
                with env('flushleft'):
                    line('\large ' + bold(project['name']) + '\\newline \\normalsize')
                    line(project['subname'] + ' ('+project['location']+') \\newline')
                    if 'special' in project: line(project['special'] + '\\newline')
                    line(project['date'])
                line('\\vspace*{-3mm}')
                if len(project['text']) > 1:
                    with env('itemize'):
                        for bullet in project['text']:
                            line('\item '+bullet);
                else:
                    line(project['text'][0])
                line(' } ')


#save to out file
with open(out_file, "w") as latex_file:
    latex_file.write("\n".join(latex_buffer))
