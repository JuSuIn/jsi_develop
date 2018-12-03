#개발자를 위한 파이썬의 연습코드

infile_name=input("Please input file name:");
outfile_name="out.log";

with open(infile_name) as infile:
    with open(outfile_name,"w") as outfile:
        for in_file in infile.readlines():
            outfile.write("read file '%s' : %s"%(infile_name,in_line));
        
