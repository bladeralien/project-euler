A = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
B = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
     'seventeen', 'eighteen', 'nineteen']
C = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty',
     'ninety']
D = A + B + C + [c + a for c in C for a in A]
E = [a + 'hundred' for a in A] + [a + 'hundred' + 'and' + d for a in A for d in D]
F = D + E
F.append('one' + 'thousand')
print(len(''.join(F)))
