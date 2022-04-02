
def analyze(lines):
  ranges = {}
  i = -1
  for line in lines:
    if line[0] == "inp": i+=1
    if line[0] == "add" and line[1] == "x" and line[2] != "z":
      num = int(line[2])
      if num <= 9:
        r1 = 1-num
        r2 = 9-num
        ranges[i] = range(min(r1, r2), max(r1,r2) + 1)
  return ranges

def varOrNum(state, a):
  if a in state.keys():
    return state[a]
  return int(a)

def run(data, lines, state):
  state = state.copy()
  for i, line in enumerate(lines):
    cmd, var = line[:2]
    if cmd == "inp":
      if not data:
        return lines[i:], state
      state[var] = int(data.pop(0))
    else:
      val = varOrNum(state, line[2])
      if cmd == "add":
        state[var] += val
      elif cmd == "mul":
        state[var] *= val
      elif cmd == "div":
        state[var] //= val
      elif cmd == "mod":
        state[var] %= val
      elif cmd == "eql":
        state[var] = int(state[var] == val)
  return [], state

def nextDigit(data, lines, state, ranges, characterRange):
  if not lines:
    if state['z'] == 0:
      return "".join(map(str,data))
    return False

  for i in characterRange:
    newLines, newState = run([i], lines, state)
    newData = data + [i]
    if len(newData) in ranges:
      if not newState['z']%26 in ranges[len(newData)]:
        continue
    res = nextDigit(newData, newLines, newState, ranges, characterRange)
    if res:
      return res

lines = [line.strip().split() for line in open("input.txt")]
initialState = {'w':0, 'x':0, 'y':0, 'z':0}
ranges = analyze(lines)
print(nextDigit([], lines, initialState, ranges, range(9,0,-1)), nextDigit([], lines, initialState, ranges, range(1,10)))
