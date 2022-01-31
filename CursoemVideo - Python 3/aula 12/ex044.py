#Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros
# By: Gustavo Vieira (X:II).
print('==================|SYSTEM COMPRAS|VISA CARD - 2022|==================')
prod = str(input('|VISA CARD| Qual produto gostaria de adquirir: '))
val_prod = float(input('|VISA CARD| Qual o valor do {}? R$'.format(prod)))
mood_pag = int(input(''' Como gostaria de pagar o seu {}?
|VISA CARD|[ 1 ] à vista dinheiro/cheque: 10% de desconto
|VISA CARD|[ 2 ] à vista no cartão: 5$ de desconto
|VISA CARD|[ 3 ] em até 2x no cartão: preço formal
|VISA CARD|[ 4 ] 3x ou mais no cartão: 20% de juros
'''.format(prod)))
if mood_pag == 1:
    val_desc = ((val_prod * 10) / 100)
    print('''==================|VISA CARD|==================
    |VISA CARD| OPÇÃO 1 - À vista dinheiro/cheque
    |VISA CARD| PRODUTO COMPRADO: {}
    |VISA CARD| VALOR A SER PAGO: R${:.2f}
    |VISA CARD| DESCONTO DE 10%: R${:.2f} '''.format(prod, (val_prod - val_desc), val_desc))
    print('==================|VISA CARD|==================')
    fim_pag = str(input('Gostaria de seguir com a compra? [sim/nao] R: '))
    if fim_pag == 'sim':
                print('===============|DADOS PAGAMENTO|===============')
                doc_cpf = str(input('INFORME CPF: '))
                doc_nome = str(input('INFORME NOME COMPLETO: '))
                doc_nasc = str(input('INFORME DATA DE NASCIMENTO: '))
                print('===============|DADOS PAGAMENTO|===============')
                pag_fim = str(input('Gostaria de confirmar a compra? R: '))
                if pag_fim == 'sim':
                    print('===============|COMPRA CONCLUIDA|===============')
                    print('''
    ===============|INFORMAÇÃO PRODUTO/COMPRADOR|===============
    |VISA CARD|Produto Comprado: {}.    
    |VISA CARD|Valor Produto: R${:.2f}
    |VISA CARD|Valor Desconto: R${:.2f}
    |VISA CARD|Valor a ser pago: R${:.2f}
    |VISA CARD|Nome comprador: {}.       
    |VISA CARD|CPF comprador: {}.        
    |VISA CARD|Data Nascimento: {}.     
    ===============|INFORMAÇÃO PRODUTO/COMPRADOR|===============
                    '''.format(prod, val_prod, val_desc, (val_prod-val_desc), doc_nome, doc_cpf, doc_nasc))
                else:
                    print('|VISA CARD|Sua compra não foi efetuada, obrigado.')
    else:
        print('|VISA CARD|Sua compra não foi efetuada, obrigado.')
        exit()
elif mood_pag == 2:
    val_desc = ((val_prod * 5) / 100)
    print('''==================|VISA CARD|==================
    |VISA CARD| OPÇÃO 2 - À vista no cartão
    |VISA CARD| PRODUTO COMPRADO: {}
    |VISA CARD| VALOR A SER PAGO: R${:.2f}
    |VISA CARD| DESCONTO DE 5%: R${:.2f} '''.format(prod, (val_prod - (val_prod *5) / 100), (val_prod * 5) / 100))
    print('==================|VISA CARD|==================')
    fim_pag = str(input('Gostaria de seguir com a compra? [sim/nao] R: '))
    if fim_pag == 'sim':
                print('===============|DADOS PAGAMENTO|===============')
                doc_cpf = str(input('INFORME CPF: '))
                doc_nome = str(input('INFORME NOME COMPLETO: '))
                doc_nasc = str(input('INFORME DATA DE NASCIMENTO: '))
                print('===============|DADOS PAGAMENTO|===============')
                pag_fim = str(input('Gostaria de confirmar a compra? R: '))
                if pag_fim == 'sim':
                    print('===============|COMPRA CONCLUIDA|===============')
                    print('''
    ===============|INFORMAÇÃO PRODUTO/COMPRADOR|===============
    |VISA CARD|Produto Comprado: {}.    
    |VISA CARD|Valor Produto: R${:.2f}
    |VISA CARD|Valor Desconto: R${:.2f}
    |VISA CARD|Valor a ser pago: R${:.2f}
    |VISA CARD|Nome comprador: {}.       
    |VISA CARD|CPF comprador: {}.        
    |VISA CARD|Data Nascimento: {}.     
    ===============|INFORMAÇÃO PRODUTO/COMPRADOR|===============
                    '''.format(prod, val_prod, val_desc, (val_prod-val_desc), doc_nome, doc_cpf, doc_nasc))
                else:
                    print('|VISA CARD|Sua compra não foi efetuada, obrigado.')
    else:
        print('|VISA CARD|Sua compra não foi efetuada, obrigado.')
        exit()
elif mood_pag == 3:
    duas_vezes = val_prod / 2
    print('''==================|VISA CARD|==================
    |VISA CARD| OPÇÃO 3 - Em até 2x no cartão
    |VISA CARD| PRODUTO COMPRADO: {}
    |VISA CARD| VALOR A SER PAGO: R${:.2f}
    |VISA CARD| EM 2x de: R${:.2f} '''.format(prod, val_prod , duas_vezes))
    print('==================|VISA CARD|==================')
    fim_pag = str(input('Gostaria de seguir com a compra? [sim/nao] R: '))
    if fim_pag == 'sim':
                print('===============|DADOS PAGAMENTO|===============')
                doc_cpf = str(input('INFORME CPF: '))
                doc_nome = str(input('INFORME NOME COMPLETO: '))
                doc_nasc = str(input('INFORME DATA DE NASCIMENTO: '))
                print('===============|DADOS PAGAMENTO|===============')
                pag_fim = str(input('Gostaria de confirmar a compra? R: '))
                if pag_fim == 'sim':
                    print('===============|COMPRA CONCLUIDA|===============')
                    print('''
    ===============|INFORMAÇÃO PRODUTO/COMPRADOR|===============
    |VISA CARD|Produto Comprado: {}.    
    |VISA CARD|Valor Produto: R${:.2f}
    |VISA CARD|Duas Vezes de: R${:.2f}
    |VISA CARD|Nome comprador: {}.       
    |VISA CARD|CPF comprador: {}.        
    |VISA CARD|Data Nascimento: {}.     
    ===============|INFORMAÇÃO PRODUTO/COMPRADOR|===============
                    '''.format(prod, val_prod, duas_vezes, doc_nome, doc_cpf, doc_nasc))
                else:
                    print('|VISA CARD|Sua compra não foi efetuada, obrigado.')
    else:
        print('|VISA CARD|Sua compra não foi efetuada, obrigado.')
        exit()
elif mood_pag == 4:
    print('''==================|VISA CARD|==================
    |VISA CARD| OPÇÃO 4 - 3x ou mais no cartão''')
    quant_vezes = int(input('    |VISA CARD| EM QUANTAS VEZES NO CARTÃO: '))
    val_acres = val_prod + ((val_prod * 20) / 100)
    varias_vezes = (val_acres / quant_vezes)
    print('''    |VISA CARD| PRODUTO COMPRADO: {}
    |VISA CARD| VALOR A SER PAGO: R${:.2f}
    |VISA CARD| EM {}x de: R${:.2f} '''.format(prod, val_acres, quant_vezes, varias_vezes))
    print('==================|VISA CARD|==================')
    fim_pag = str(input('Gostaria de seguir com a compra? [sim/nao] R: '))
    if fim_pag == 'sim':
                print('===============|DADOS PAGAMENTO|===============')
                doc_cpf = str(input('INFORME CPF: '))
                doc_nome = str(input('INFORME NOME COMPLETO: '))
                doc_nasc = str(input('INFORME DATA DE NASCIMENTO: '))
                print('===============|DADOS PAGAMENTO|===============')
                pag_fim = str(input('Gostaria de confirmar a compra? R: '))
                if pag_fim == 'sim':
                    print('===============|COMPRA CONCLUIDA|===============')
                    print('''
    ===============|INFORMAÇÃO PRODUTO/COMPRADOR|===============
    |VISA CARD|Produto Comprado: {}.    
    |VISA CARD|Valor Produto: R${:.2f}
    |VISA CARD|Valor final Produto: R${:.2f}
    |VISA CARD|Em {}x de: R${:.2f}
    |VISA CARD|Nome comprador: {}.       
    |VISA CARD|CPF comprador: {}.        
    |VISA CARD|Data Nascimento: {}.     
    ===============|INFORMAÇÃO PRODUTO/COMPRADOR|===============
                    '''.format(prod, val_prod, val_acres, quant_vezes, varias_vezes, doc_nome, doc_cpf, doc_nasc))
                else:
                    print('|VISA CARD|Sua compra não foi efetuada, obrigado.')
    else:
        print('|VISA CARD|Sua compra não foi efetuada, obrigado.')
        exit()
else:
    print('Opção invalida, tente novamente.')
