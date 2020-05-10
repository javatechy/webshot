from tabulate import tabulate

table = [["Sun",696000,1989100000],["Earth",6371,5973.6],  ["Moon",1737,73.5],["Mars",3390,641.85]]


print(tabulate(table, headers=["Planet","R (km)", "mass (x 10^29 kg)"]))

table.sort(key=lambda x: x.duration)
print(tabulate([[
        "  {color}{author}{end}  ".format(
            color=(BColor.BOLD if result.submission.author == CONFIG.user else BColor.GREEN),
            author=result.submission.author,
            end=BColor.ENDC),

        "  {color}{answer}{end}  ".format(
            color=(BColor.BOLD if result.submission.author == CONFIG.user else BColor.BLUE),
            answer=result.answer,
            end=BColor.ENDC),

        "  {color}{msecs:8.2f} ms{end}".format(
            color=BColor.BOLD,
            msecs=result.duration,
            end=BColor.ENDC),

        "  {color}{language}{end}".format(
            color=(BColor.BOLD if result.submission.author == CONFIG.user else ""),
            language=result.submission.language,
            end=BColor.ENDC,
        )
    ] for result in table]))