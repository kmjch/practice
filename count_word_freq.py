# -*- coding: utf-8 -*-

from collections import Counter


def count_word_freq(text):
    for a, b in Counter(text.lower().split()).most_common():
        print a, b
    return "finished"

print count_word_freq("Since 2012, Instacart has rapidly expanded to 25+ markets \
and partnered with 100+ retailers. Our mission is to transform everyday life by \
seeking and solving seemingly impossible problems. Instacart is the only grocery \
service that delivers in as little as one hour. By combining a personal touch \
with cutting-edge technology, Instacart offers customers a simple solution to \
save time and buy directly from the retailers they trust. We give customers back \
their time so they can do more of what they love. \
Responsibilities \
As a Catalog team member, you will be the data backbone and project management \
link supporting Instacart’s partner and operational priorities. You will be the \
primary technical point of contact with numerous retailer partners across the \
country. Working at the edge of expansion -- supporting and refining existing \
operations -- you will own the launching of new partners and markets. \
You are the perfect mix of analytical, technical, and operational: pulling, \
sanitizing, and analyzing data; applying critical thinking to make recommendations ; \
and informing major catalog and operations decisions. Catalog team members work \
cross-functionally with our world-class Engineering, Business Development, and \
Operations teams. \
You will be an expert on Instacart’s data processing systems and act as a \
resource for other team members across the nation in the diagnosis, planning, \
and execution of data catalog projects. \
Requirements \
2-4 years work experience in a relevant field with demonstrated cross-functional \
and collaborative project or team management experience \
Polished communication skills and comfort working with internal and external \
stakeholders including major retailers and CPG companies \
Proficient in SQL, advanced Excel, and/or other data visualization tools to deep \
dive into data, identify and quantify opportunities, and design sustainable \
improvements and solutions \
Proven track record of designing and implementing process improvement projects \
from start to finish in a resource-constrained environment \
A strong analytical skill set, comfortable manipulating large data sets and an \
understanding of databases and data integrity principles \
Proven success working in teams \
A self-starter with the ability to quickly respond to problems independently \
A strong sense of ownership in your work")
