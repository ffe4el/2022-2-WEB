import os.path


def input_dan(prompt):
    return prompt

def main():
    output_dir ="../HW04/output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    dan = 6
    color = "cyan"
    with open(os.path.join(output_dir,"gugu_show.html"),"w" ) as f:
        f.write("<html>\n")
        f.write("<body>")

        for i in range(9):
            f.write(f"{dan} * {i+1} = <font color='{color}'> {dan*(i+1)}</font><br>\n")

        f.write("</body>")
        f.write("</html>")

if __name__ == "__main__":
    main()