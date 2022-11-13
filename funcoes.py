from random import randint

def transforma_base(que):
    d = {}
    for q in que:
        d1 = q['nivel']
        if d1 not in d:
            d[d1] = []
        d[d1].append(q)

    return d

def valida_questao(que):
    v = {}
    if len(que) != 4:
        v['outro'] = 'numero_chaves_invalido'
    p = ['titulo','nivel','opcoes','correta']
    for k in p:
        if k not in que:
            v[k] = 'nao_encontrado'
    if 'titulo' in que:
        t = que['titulo'].strip()
        if len(t) == 0:
            v['titulo'] = 'vazio'
    d1 = ['facil','medio','dificil']
    if 'nivel' in que:
        if que['nivel'] not in d1:
            v['nivel'] = 'valor_errado'
    if 'opcoes' in que:
        f = False
        if len(que['opcoes']) != 4:
            v['opcoes'] = 'tamanho_invalido'
        else:
            f = True
        if f == True:
            va = True
            o = ['A','B','C','D']
            if len(que['opcoes']) != 4:
                v['opcoes'] = 'chave_invalida_ou_nao_encontrada'
                va = False
            for a in que['opcoes']:
                if a not in o:
                    v['opcoes'] = 'chave_invalida_ou_nao_encontrada'
                    va = False
            if va == True:
                for a in o:
                    r = que['opcoes'][a].strip()
                    if len(r) == 0:     
                        if 'opcoes' not in v:
                            v['opcoes'] = {}
                        v['opcoes'][a] = 'vazia'
    o = ['A','B','C','D']
    if 'correta' in que:
        if que['correta'] not in o:
            v['correta'] = 'valor_errado'
    return v
    
def valida_questoes(que):
    e =[]
    for q in que:
        dicionario = valida_questao(q)
        e.append(dicionario)
    return e

def sorteia_questao(que,n):
    ques = que[n]
    sorteio = randint(0,len(ques)-1)
    return ques[sorteio]

def sorteia_questao_inedita(que,n,sorteio1):
    while True:
        q = sorteia_questao(que,n)
        if q not in sorteio1:
            sorteio1.append(q)
        break
    return q

def questao_para_texto(que,iq):
    dicionario1 = '----------------------------------------\nQUESTAO {0}\n\n{1}\n\nRESPOSTAS:\nA: {2}\nB: {3}\nC: {4}\nD: {5}\n'.format(iq,que['titulo'],que['opcoes']['A'],que['opcoes']['B'],que['opcoes']['C'],que['opcoes']['D'])
    return dicionario1 

def gera_ajuda(que):
    na = randint(1,2)
    nl = {1:'A',2:'B',3:'C',4: 'D'}
    tirou = []

    c = que['correta']

    while na != 0:
        tira = nl[randint(1,4)]
        if tira!= c and tira not in tirou:
            na -= 1
            tirou.append(que['opcoes'][tira])

    if len(tirou) == 2:
        return 'DICA:\nOpções certamente erradas: {0} | {1}'.format(tirou[0],tirou[1])
    if len(tirou) == 1:
        return'DICA:\nOpções certamente erradas: {0}'.format(tirou[0])