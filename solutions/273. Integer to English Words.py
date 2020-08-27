class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: return 'Zero'
        self.words = {100:('One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'),
                      10:('Onety','Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'), 
                      1:('One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine')}
​
        self.exc = {10:'Ten',11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 
                    15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen'}
        check = ((1000000000, 'Billion'), (1000000, 'Million'), (1000,'Thousand'), (1, ''))
        self.result = []
        
        for x, rank in check:
            if num > x-1:
                self.hundredsText(num//x)
                if rank: self.result.append(rank)
                num %= x
        return ' '.join(self.result)
        
    def hundredsText(self, num):
        check = ((100, ' Hundred'), (10, ''), (1, ''))
        for x, rank in check:
            if num > 9 and num < 20:
                self.result.append(self.exc[num])
                break
            if num > x-1:
                self.result.append(self.words[x][num//x-1] + rank)
                num %= x
