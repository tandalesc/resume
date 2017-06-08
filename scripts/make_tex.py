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
    def __init__(self, env_name, latex, env_arg=None, skip_ending=False):
        self.env_name = env_name; self.env_arg = env_arg; self.latex = latex
        self.skip_ending = skip_ending
    def __enter__(self):
        latex_str = "\\begin{"+self.env_name+"}"
        if self.env_arg is not None: latex_str += "{"+self.env_arg+"}"
        self.latex(latex_str)
        self.latex.tabs += 1
    def __exit__(self, exc_type, exc_value, traceback):
        self.latex.tabs -= 1
        if not self.skip_ending: self.latex("\\end{"+self.env_name+"}")
bold = lambda text: "\\textbf{"+text+"}"

#parse attributes from yaml to latex lines and envs
with open(in_file, "r") as yaml_file:
    latex_buffer = []
    line = latex_data(latex_buffer)
    env = lambda e,args=None: latex_env(e, line, env_arg=args)
    spec = yaml.load(yaml_file)

    line("\documentclass{article}")
    line("\\usepackage[utf8]{inputenc}")
    line("\\usepackage{multicol}")
    line("\\usepackage[top=1in, bottom=1in, left=1in, right=1in]{geometry}")
    line("\\title{"+spec['header']['name']+"}")
    line("\\author{"+spec['header']['email']+"}")
    line("\date{"+spec['header']['phone']+"}")
    with env('document'):
        line("\maketitle")
        with env('multicols*','2'):
            line("\section*{Education}")
            with env('flushleft'):
                for school in spec['education']:
                    line('\par' + bold(school['name'])+ '\\newline')
                    line(school['degree'] + '\\newline')
                    line(school['date'] + '\\newline')
                    line('\smallskip')

#save to out file
with open(out_file, "w") as latex_file:
    latex_file.write("\n".join(latex_buffer))
