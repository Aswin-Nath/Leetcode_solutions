memo={}
# prev-condition_based_var
def back(ind,prev):
  if (ind,prev) in memo:
    return memo[(ind,prev)]
  if ind==len(s):
    return 0
  pick=float("-inf")
  npick=back(ind+1,prev)
  if prev is None or abs(ord(s[ind])-prev)<=k:
    pick=back(ind+1,ord(s[ind]))+1
  memo[(ind,prev)]=max(pick,npick)
  return memo[(ind,prev)]
        
