{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[{"file_id":"12dAcIUICiG_ejaxVJcDMay1CZMaZ9LgJ","timestamp":1699469106746}],"authorship_tag":"ABX9TyPdll0ASgaD058wt43Vb1Z9"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":null,"metadata":{"id":"20jqCE0Rg7TM"},"outputs":[],"source":["theBoard = {'top-L':'','top-M':'','top-R':'',\n","            'mid-L':'','mid-M':'','mid-R':'',\n","            'low-L':'','low-M':'','low-R':''}\n","\n","def printBoard(board):\n","  print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])\n","  print('-+-+-')\n","  print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])\n","  print('-+-+-')\n","  print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])\n","turn = 'X'\n","for i in range(9):\n","  printBoard(theBoard)\n","  print('Turn for ' + turn + '. Move on which space?')\n","  move = input()\n","  theBoard[move] = turn\n","  if turn == 'X':\n","    turn = 'O'\n","  else:\n","    turn ='X'\n","print(Board(theBoard))\n"]}]}