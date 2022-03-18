#!/usr/bin/env python
# coding: utf-8

# In[24]:


import re
 
#檢查分析片段是否為合法字元
def inputCheck (seq):
    if re.match("^[ATCG]*$",seq) != None and len(seq)>0:
        return True
    else:
        return False
    
#檢查尋找序列是否為合法字元    
def searchCheck (seq):
    if re.match("^[ATCGRYSWKMBDHVN]*$",seq) != None and len(seq)>0:
        return True
    else:
        return False
 
def check():
    inputSeq = input('分析序列 (只允許 ATCG): \n').upper()
    if inputCheck(seq = inputSeq):
        print(f'分析序列長度為: {len(inputSeq)} nt\n')
        searchSeq = input('尋找片段 (允許所有 IUPAC codes): \n').upper()
        if searchCheck(seq = searchSeq):
            print(f'尋找片段長度為: {len(searchSeq)} nt\n')
            if len(inputSeq) >= len(searchSeq):
                print('分析結果:')
                return inputSeq, searchSeq
            else:
                print('終止分析: 分析序列長度不得小於尋找片段')
                return False
        else:
            print('終止分析: 尋找片段異常')
            return False
    else:
        print('終止分析: 分析序列異常')
        return False
        

def convertion(seq):
    seq=list(seq)
    for c in range(len(seq)):
        if seq[c] == 'N':
            seq[c] = 'ATCG'
        elif seq[c] == 'V':
            seq[c] = 'ACG'
        elif seq[c] == 'H':
            seq[c] = 'ACT'
        elif seq[c] == 'D':
            seq[c] = 'AGT'
        elif seq[c] == 'B':
            seq[c] = 'CGT'
        elif seq[c] == 'M':
            seq[c] = 'AC'
        elif seq[c] == 'K':
            seq[c] = 'GT'
        elif seq[c] == 'W':
            seq[c] = 'AT'
        elif seq[c] == 'S':
            seq[c] = 'GC'
        elif seq[c] == 'Y':
            seq[c] = 'CT'
        elif seq[c] == 'R':
            seq[c] = 'AG'
    return seq
        
def searching(inputSeq, searchSeq):

    hitSeq = []
    search_No = 0
    for nt in range(len(inputSeq)-(len(searchSeq)-1)):
        hits = 0
        for hit in range(len(searchSeq)):
            #print(f'{inputSeq[nt+hit]} in {searchSeq[hit]}?')
            if inputSeq[nt+hit] in searchSeq[hit]:
                hits += 1
#                print('Yes\n')
            else:
                pass
#                print('No\n')
        if hits == len(searchSeq):
            search_No += 1
            hitSeq.append(inputSeq[nt: (nt+(len(searchSeq)))])
#    print(hitSeq)
#    print(search_No)
    return hitSeq, search_No

def show_hits (hitSeq, searchSeq, inputSeq):
    print(f'有 {len(hitSeq)} 個 {searchSeq} site(s):')
    set_hits = set(hitSeq)
    outputSeq = inputSeq.lower()
    if len(hitSeq) != 0:
        for sets_show in set_hits:
            print(f'{sets_show} 有 {hitSeq.count(sets_show)} 個')
            outputSeq = outputSeq.replace(sets_show.lower(), sets_show.upper())
        print(f'\n大寫處為 {searchSeq} 序列:\n{outputSeq}')
    else:
        print('\n(此序列不存在尋找片段)')

def main():
    inputs = check()
    if inputs != False:
        inputSeq = inputs[0]
        searchSeq = inputs[1]
        searchSeqCon = convertion(list(inputs[1]))
        search = searching(inputSeq, searchSeqCon)
        hitSeq = search[0]
        hitNo = search[1]
        show_hits(hitSeq, searchSeq, inputSeq)
 
if __name__ == '__main__':
    main()


# In[ ]:




