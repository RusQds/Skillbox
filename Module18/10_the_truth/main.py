alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
step_list = list(range(1,2))
new_text = ''
new_text_list = []
step = 3
print('#' * 30)
print('Изначальный текст: {}'.format(text))
print('#' * 30)

for word in text.split():
    new_elem = '{0}{1}'.format(word[step * (-1) % len(word):], word[:(len(word) - step) % len(word)])
    if new_elem[-1] != '/':
        new_text_list.append(new_elem)
    else:
        new_text_list.append('\n')
        step += 1

new_text = ' '.join(new_text_list)

for i_step in step_list:
    new_text_list.clear()
    for sym in new_text:
        if sym in alphabet_lower:
            new_text_list.append(alphabet_lower[abs((alphabet_lower.index(sym) - i_step) % len(alphabet_lower))])
        elif sym in alphabet_upper:
            new_text_list.append(alphabet_upper[abs((alphabet_upper.index(sym) - i_step) % len(alphabet_upper))])
        else:
            new_text_list.append(sym)

    new_text = ''.join(new_text_list)

print('Расшифрованный текст: {}'.format(new_text))



