# -*- coding: UTF-8 -*-
import time

def init(line):
    f = open("header.txt")
    cpy = f.read()
    out.write(cpy)
    f.close()
    out.write("  <title>"+line[2:-1]+"</title>\n")
    f = open("header1.txt")
    cpy = f.read()
    out.write(cpy)
    f.close()

def end():
    f = open("footer.txt")
    cpy = f.read()
    out.write(cpy)
    f.close()

def start_section(line):
    out.write("      <div class=""tm-content-container"">"+"\n")
    out.write("        <div class=""tm-content"">"+"\n")

def end_section():
    out.write("        </div>\n")
    out.write("      </div>\n")

inp = open("in.md")
lines = inp.readlines()
inp.close()
out = open("out.html", "w")

in_section = 0
indent = 0
in_ul = 0
for line in lines:
    if(line.find("- ") != 0 and in_ul):
        out.write("          </ul>\n")
        in_ul = 0
    if(line.find("# ") == 0):
        init(line)
    elif(line.find("## ") == 0):
        out.write("          <h2 class=""tm-page-title"">"+line[3:-1]+"</h2>\n")
    elif(line.find("### ") == 0):
        out.write("          <p class=""mb-4"">"+line[4:-1]+"</p>\n")
    elif(line.find("date--") == 0):
        out.write("          <p class=""date"">last modified: "+time.strftime("%b. %d, %Y", time.localtime())+"</p>\n")
    elif(line.find("---") == 0):
        if(in_section):
            end_section()
        start_section(line)
        in_section = 1
    elif(line.find("- ") == 0):
        if(in_ul == 0):
            out.write("          <ul>\n")
            in_ul = 1
        out.write("            <li>"+line[2:-1]+"</li>\n")
    else:
        out.write("          <p>\n")
        out.write("            "+line[0:-1]+"\n")
        out.write("          </p>\n")
if(in_ul):
    out.write("          </ul>\n")
    in_ul = 0
if(in_section):
    end_section()
end()
out.close()