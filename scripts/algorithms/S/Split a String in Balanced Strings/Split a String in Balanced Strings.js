var balancedStringSplit = function(s) {
    let r_count = 0;
    let l_count = 0;
    let ans =0;
    for(let i = 0 ; i < s.length;i++){
        if(s[i]==='R') r_count++;
        else l_count++;
        
        if(l_count==r_count) {
         l_count=0
        r_count=0;   
            ans++
        }
        
    }
    return ans
};
