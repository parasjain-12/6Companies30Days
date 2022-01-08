class TrieNode:
  
    #    Constructor
    def __init__(self):
        
        self.children = [None] * 26
            
        i = ord('a')
        while i <= ord('z'):
            self.children[i - ord('a')] = None;
            i += 1
            
        self.isEnd = False
        

def insertContact(str, root):
    n = len(str)

    itr = root

    for i in range(n):
        
        #    Check if the str[i] is already present in our Trie.
        if itr.children[ord(str[i]) - ord('a')] == None:
            
            #   If not found then create a new TrieNode
            itr.children[ord(str[i]) - ord('a')] = TrieNode()
            
        nextNode = itr.children[ord(str[i]) - ord('a')]
        
        #    Move the iterator('itr') to point to next Trie Node.
        itr = nextNode 

        #    If its the last character of the string 'str' then mark 'isEnd' as true
        if (i == n - 1):
            itr.isEnd = True

def viewSuggestionsHelper(curr, prefix, temp):
    
    #    Check if the string 'prefix' ends at this Node If yes then display the string found so far
    if (curr.isEnd == True):
        temp.append(prefix)

    #    Find all the adjacent Nodes to the current Node and then call the function recursively.
    c = ord('a')
    while c <= ord('z'):
        if curr.children[c - ord('a')] != None:
            prefix += chr(c)
            viewSuggestionsHelper(curr.children[c - ord('a')], prefix, temp)
            prefix = prefix[:-1]
        c += 1

def viewSuggestions(str, root):
    
    prev = root

    prefix = ""

    n = len(str)
    
    result = []

    for i in range(n):
        
        #    'prefix' stores the string formed so far.
        prefix += str[i]

        #    Get the last character entered.
        lastCharacter = prefix[i]
        
        #    Find the Node corresponding to the last character of 'prefix' which is pointed by prev of the Trie.
        if ord(lastCharacter) - ord('a') >= 0 and prev.children[ord(lastCharacter) - ord('a')] != None:
            curr = prev.children[ord(lastCharacter) - ord('a')]
        else:
            
            #    If nothing found, then break the loop as no more prefixes are going to be present.
            break
        
        
        #    If present in trie then insert all the contacts with given prefix in the result.
        temp = []

        viewSuggestionsHelper(curr, prefix, temp)

        result.append(temp)

        #    Change prev for next prefix
        prev = curr
    
    return result

def insertContactList(contactList, root):

    n = len(contactList)

    #    Insert each contact into the trie.
    for i in range(n):
        insertContact(contactList[i], root)

def phoneDirectory(contactList, queryStr):

    root = TrieNode()

    #    Insert all the Contacts into Trie.
    insertContactList(contactList, root)

    #    Return the corresponding suggestions.
    return viewSuggestions(queryStr, root)
