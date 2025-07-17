# xking_interpreter.py
# Simple interpreter for Xking language

def run_xking_code(code):
    lines = code.strip().splitlines()
    for line in lines:
        if line.startswith("say "):
            print(line[4:].strip('"'))

if __name__ == "__main__":
    with open("examples/hello.xking", "r") as f:
        code = f.read()
    run_xking_code(code)
