file1 = open('higgs-mention_network.edgelist.txt', 'r')
file2 = open('higgs-reply_network.edgelist.txt', 'r')
file3 = open('higgs-retweet_network.edgelist.txt', 'r')
print len(file1.readlines())+ len(file2.readlines()) + len(file3.readlines())