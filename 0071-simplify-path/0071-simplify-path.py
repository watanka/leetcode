class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        . : current directory
        ../ : up a level
        // : /
        any other format : file/directory name
        '''

        splitted = path.replace('//', '/').split('/')[1:]
        answer = []
        stack = []
        for name in splitted :
            
            if name == '..' : 
                if not stack :
                    stack = []
                else :
                    stack.pop()
            elif name != '' and name != '.' :
                stack.append(name)
                

        return '/' + '/'.join(stack)