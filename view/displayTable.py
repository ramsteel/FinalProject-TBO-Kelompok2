
def printFillingTable(stTable, footer):
    htmlTableSyntax = ''
    for x in range(len(stTable)):
        i = 0
        htmlTableSyntax += '<tr align="center" style=font-size:12px>'
        for j in range((len(stTable)-1)-x, len(stTable)):
            htmlTableSyntax += ('<td>' + stTable[i][j] + '</td>')
            i+=1
        htmlTableSyntax += '</tr>'

    htmlTableSyntax += '<tr align="center" style=font-size:14px>'
    for i in range(len(footer)):
        htmlTableSyntax+=('<th style=color:green>' + footer[i] + '</th>')
    
    htmlTableSyntax+='</tr>'

    return htmlTableSyntax