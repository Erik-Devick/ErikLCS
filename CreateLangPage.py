langs = ["Java","Python","Python3","C","C#","JavaScript","TypeScript","PHP",
         "Swift","Kotlin","Dart","Go","Ruby","Scala","Rust","Racket","Erlang","Elixer"]

def run(lang):
    fout = lang+".html"
    html = f"""
        <!DOCTYPE html>
        <html lang="en">
            <link rel="stylesheet" href="https://erik-devick.github.io/ErikLCS/style.css">
            <body>
                <h1 class="mainHeader">{lang}</h1>
                <input id="searchbar" onkeyup="search_problem()" type="text" name="search" placeholder="Search Problem">
                <ul id="list" style="list-style: none;">

                </ul>
                <script src="https://erik-devick.github.io/ErikLCS/problems.js"></script>
            </body>
        </html>"""

    with open(fout,"w") as outfile:
        print(html,file=outfile)

for l in langs:
    run(l)