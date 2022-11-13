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