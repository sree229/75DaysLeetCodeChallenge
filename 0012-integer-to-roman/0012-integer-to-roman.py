class Solution:
    def intToRoman(self, num: int) -> str:
        Roman = ""
        while num!=0 :
            if num>=1000 :
                Roman += "M"
                num = num-1000
            elif num>=900 :
                Roman += "CM"
                num = num-900
            elif num>=500 :
                Roman += "D"
                num =  num-500
            elif num>=400 :
                Roman += "CD"
                num =  num-400
            elif num>=100:
                Roman += "C"
                num =  num-100
            elif num>=90 :
                Roman += "XC"
                num =  num-90
            elif num>=50:
                Roman += "L"
                num = num-50
            elif num>=40 :
                Roman += "XL"
                num =  num-40
            elif num>=10 :
                Roman += "X"
                num = num-10
            elif num>=9 :
                Roman += "IX"
                num = num-9
            elif num>=5 :
                Roman += "V"
                num =  num-5
            elif num>=4 :
                Roman += "IV"
                num = num-4
            elif num>=1 :
                Roman += "I"
                num =  num-1
            else :
                pass
        return Roman
            
            