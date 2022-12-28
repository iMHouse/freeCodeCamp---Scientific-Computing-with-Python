def arithmetic_arranger(problems, showResult = False):
  arranged_problems = ""

  problemsDetails = dict()

  firstRow = list()
  secondRow = list()
  thirdRow = list()
  results = list()
  
  if len(problems) > 5:
    return "Error: Too many problems."

  for problem in problems:
    problemsDetails[problem] = dict()

    problemParts = problem.split()

    if problemParts[1] not in ["+", "-"]:
      return "Error: Operator must be '+' or '-'."

    if not (problemParts[0].isdigit() and problemParts[2].isdigit()):
      return "Error: Numbers must only contain digits."

    if len(problemParts[0]) > 4 or len(problemParts[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
    
    maxLength = len(problemParts[0]) if len(problemParts[0]) > len(problemParts[2]) else len(problemParts[2])
    problemLength = maxLength + 2

    firstRow.append(problemParts[0].rjust(problemLength))
    secondRow.append(problemParts[1] + problemParts[2].rjust(problemLength - 1))
    thirdRow.append("-" * problemLength)
    results.append(str(eval(problem)).rjust(problemLength))

  arranged_problems = arranged_problems + "    ".join(firstRow) + "\n"
  arranged_problems = arranged_problems + "    ".join(secondRow) + "\n"
  arranged_problems = arranged_problems + "    ".join(thirdRow)
  if showResult:
    arranged_problems = arranged_problems + "\n"
    arranged_problems = arranged_problems + "    ".join(results)
  return arranged_problems