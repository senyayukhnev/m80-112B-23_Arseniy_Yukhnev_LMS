peter = float(input())
vasya = float(input())
tolya = float(input())
participant = [peter, vasya, tolya]
winner = max(participant)
second = sum(participant) - max(participant) - min(participant)
third = min(participant)
if winner == peter:
    winner = 'Петя'
if winner == vasya:
    winner = 'Вася'
if winner == tolya:
    winner = 'Толя'
if second == peter:
    second = 'Петя'
if second == vasya:
    second = 'Вася'
if second == tolya:
    second = 'Толя'
if third == peter:
    third = 'Петя'
if third == vasya:
    third = 'Вася'
if third == tolya:
    third = 'Толя'
print(f'         {winner}          ')
print(f' {second}  ')
print(f'                  {third}  ')
print('   II      I      III   ')