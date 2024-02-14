N1, N2 ,N3, N4 = map(float,input().split())
ave = (N1*2+N2*3+N3*4+N4)/10
print(f"Media: {(ave):.1f}")
if ave>=7.0:
    print("Aluno aprovado.")
elif ave<5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exam_score=float(input())
    print(f"Nota do exame: {exam_score:.1f}")
    new_ave = (exam_score+ave)/2
    if new_ave>=5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {(new_ave):.1f}")
