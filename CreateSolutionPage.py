import re
import subprocess
import time

def makeListItem(language, probNum, probName):
    newProb = (f'<li class="problems"><a href="https://erik-devick.github.io/ErikLCS/{str(language)}/{str(probNum)}.html">{str(probNum)}. {str(probName)}</a></li>')
    infile = open(".\\"+language+".html","r")
    problemList = []
    listItem = re.compile(r'class="problems"')
    for line in infile:
        line = line.strip()
        if listItem.findall(line) != []:
            problemList.append(line)
    infile.close()
    probNums = []
    for problem in problemList:
        index = problem.find(".html")
        problem = problem[index+7:]
        periodIndex = problem.find(".")
        num = problem[:periodIndex]
        probNums.append(num)

    counter = 0
    for entry in probNums:
        if int(entry) < int(probNum):
            counter += 1
        else:
            break
    insertionPoint = counter

    problemList.insert(insertionPoint,newProb)


    htmlFront = f"""
    <!DOCTYPE html>
    <html lang="en">
        <link rel="stylesheet" href="https://erik-devick.github.io/ErikLCS/style.css">
        <body>
            <h1 class="mainHeader">{language}</h1>
            <input id="searchbar" onkeyup="search_problem()" type="text" name="search" placeholder="Search Problem">
            <ul id="list" style="list-style: none;">
"""
    htmlBack = """
            </ul>
            <script src="https://erik-devick.github.io/ErikLCS/problems.js"></script>
        </body>
    </html>
    """
    htmlMid = ""
    for problem in problemList:
        htmlMid += "\t\t\t\t"
        htmlMid += problem
        htmlMid += "\n"

    html = htmlFront+htmlMid+htmlBack

    outfile = open(".\\"+language+".html","w")
    print(html, file=outfile)
    outfile.close()


def makeSolutionPage(language, probNum, probName,code):
    code = code.strip()
    htmlFront = f"""
    <!DOCTYPE html>
    <html lang="en">
        <link rel="stylesheet" href="https://erik-devick.github.io/ErikLCS/style.css">
        <head>
            <title>{probName}</title>
        </head>
        <body>
            <h1 class="smallHeader">{probNum}. {probName}</h1> 
            <pre class="container">
                <code>
"""
    htmlBack = """
                </code>
            </pre>
        </body>
    </html>
    """
    outfile = open(".\\"+language+"\\"+str(probNum)+".html","w")
    print(htmlFront+code+htmlBack, file=outfile)


#CHANGE THIS WHEN MAKING PAGE
"""
Python3, C++
"""
language = "C++"
probNum = 1
probName = "Two Sum"
code = """
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        for (int i = 0; i < nums.size(); i++)
            for (int j = 0; j < nums.size(); j++)
                if (nums[1] + nums[j] == target)
                    return [i,j]
    }
};
"""


makeListItem(language,probNum,probName)
makeSolutionPage(language,probNum,probName,code)

time.sleep(3)
subprocess.run("git pull --rebase")
time.sleep(3)
subprocess.run("git add .")
time.sleep(3)
subprocess.run("git commit -m initialcommit")
time.sleep(3)
subprocess.run("git push origin main")

"""
git pull --rebase
git add .
git commit -m initialcommit
git push origin main
"""