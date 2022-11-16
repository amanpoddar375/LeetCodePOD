// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        long int l;
        long int h = n;
        long int m;
        while(l<=h){
            m = (h+l)/2;
            if(isBadVersion(m)){
                h = m-1;
            }
            else{
                l = m+1;
            }
        }
        return l ;
        }

    };
