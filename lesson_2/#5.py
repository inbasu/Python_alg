def ascii_list(start, end):
   result = ''
   row = 0
   for i in range(start, end):
      result += f' {i}: {chr(i)}; '
      row += 1
      if not row % 10:
         row = 0
         result += '\n'
   return result


if __name__ == '__main__':
   print(ascii_list(1, 123))

