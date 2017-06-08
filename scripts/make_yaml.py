# Shishir Tandale

from argparse import ArgumentParser
import yaml

parser = ArgumentParser()
parser.add_argument("-out")
args = parser.parse_args()
out_file = args.out

#fields used in yaml
header = "header"
name = "name"
phone = "phone"
email = "email"
education = "education"
date = "date"
degree = "degree"
skills = "skills"
work = "work"
projects = "projects"

#doc dict
doc = {
    header: {
        name: "Shishir Tandale",
        phone: "(571)439-6069",
        email: "shishir@tandale.com"
    },
    education: [
        {
            name: "University of Virginia",
            date: "Aug 2015 - May 2017",
            degree: "B.S. in Computer Science"
        },
        {
            name: "Virginia Commonwealth University",
            date: "Aug 2013 - May 2015",
            degree: "Pure Mathematics, Computer Science"
        }
    ],
    skills: [

    ],
    work: [

    ],
    projects: [

    ]
}

with open(out_file, "w") as yaml_file:
    yaml_file.write(yaml.dump(doc))
