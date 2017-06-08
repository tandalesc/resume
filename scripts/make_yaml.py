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
subname = "subname"
phone = "phone"
email = "email"
education = "education"
date = "date"
degree = "degree"
skills = "skills"
work = "work"
projects = "projects"
position = "position"
location = "location"
text = "text"
special = "special"


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
    skills: {
        'Programming': {
            'Over 5000 Lines': ['Python', 'Java'],
            'Over 1000 Lines': ['C++', 'PHP', 'C\#', 'CSS', 'JS/jQuery', 'C'],
            'Familiar': ['Scala', 'Ruby', 'MySQL']
        },
        'Coursework': {
            '@ UVA': [
                'Database Systems', 'Algorithms', 'Web Application Programming',
                'Defense Against the Dark Arts', 'Artifial Intelligence',
                'Computer Vision', 'Computer Graphics'
            ],
            '@ VCU': [
                'Theory of Computation', 'Object-Oriented Programming', 'Combinatorics',
                'Linear Algebra', 'Differential Equations', 'Software Engineering Practicum'
            ]
        }
    },
    work: [
        {
            name: "Commonwealth Computer Research",
            position: "Data Science Intern",
            date: "May 2016 - Aug 2016",
            location: "Charlottesville, VA",
            text: [
                "Prepared and processed geospacial and cultural datasets with tools such as Hadoop, Accumulo, GeoServer, GeoMesa, Solr, Python, Bash scripts, Scala/Java",
                "Worked on integrating multiple data sources togetherfor a unified search and mapping interface on a distributed system using technologies like GeoTools, Accumulo, and Solr",
                "Created a complex stylesheet for an interactive map using the GeoServer CSS extension. Was used in product demonstrations; will continue to be maintained",
                "Refactored existing code and created new modules using tools such as Maven, GitHub, and Artifactory"
            ]
        },
        {
            name: "Arlington Public Schools",
            position: "Enterprise Solutions Intern",
            date: "June 2015 - August 2015",
            location: "Arlington, VA",
            text: [
                "Documented Synergy procedures using Oracle UPK",
                "Assisted in training development team in C\# for API development",
                "Learned about the structure of a data-driven software stack that incorporates tools such as Oracle databases, Microsoft SQL Server, Microstrategy, and Synergy"
            ]
        }
    ],
    projects: [
        {
            name: "Natural Language Processing",
            subname: "Undergraduate Thesis",
            date: "Aug 2016 - May 2017",
            location: "Charlottesville, VA",
            special: "Advisor: Dr. Kai-Wei Chang",
            text: [
                "Performed NLP tasks on a large Twitter data-set. Built data processing pipeline in\
                Python3 and TensorFlow. Designed Twitter JSON processing pipeline, used data in a\
                feed-forward classifier and two generative models using both recurrent neural\
                networks and a custom design based on transposed convolutions, adversarial\
                auto-encoders, and the Wasserstein objective on the encoderto make the model\
                robust over noisy text data"
            ]
        },
        {
            name: "Image Super-Resolution",
            subname: "Group Project",
            date: "April 2017 - May 2017",
            location: "Charlottesville, VA",
            text: [
                "Worked on implementing image super-resolution in a small group using Python3 and\
                Keras. Designed generative adversarial network based on DCGAN and improved it\
                with the Wasserstein objective over a small flower data-set"
            ]
        },
        {
            name: "C\# Neural Network Library",
            subname: "Independant Research",
            date: "June 2015 - Aug 2015",
            location: "Arlington, VA",
            text: [
                "Designed and implemented a fully-connected neural network based on current\
                techniques using C\#. Worked on hyper-parameter optimization, intelligent bias and\
                weight initialization, stochastic statistical learning theory, and popular optimizations\
                to gradient descent. Implemented custom linear algebra libraries with a few simple\
                optimizations to reduce memory footprint"

            ]
        },
        {
            name: "Aberration",
            subname: "Independant Research",
            date: "June 2012 - May 2013",
            location: "Chantilly, VA",
            text : [
                "De-compiled and customized stock software package forthe Samsung Galaxy S2\
                mobile phone (i9100 and i777 models) and developed Android application to manage\
                advanced device settings. Developed method for deploying updates over-the-air\
                through the mobile app, and back-ported some features from newer Samsung phones"
            ]
        }
    ]
}

with open(out_file, "w") as yaml_file:
    yaml_file.write(yaml.dump(doc))
