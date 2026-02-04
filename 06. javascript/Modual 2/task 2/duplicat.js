let array=[2,2,6,3,5,1,4,5,3,5];
for(let i=0;i<array.length;i++){
    if(array[i]==0){
        continue;
    }
    let count=0;
    for(let j=i+1;j<array.length;j++){
        if(array[i]==array[j]){
            count++;
            array[j]=0;
        }
        
    }
    if(count>0){
        console.log(`the duplicate values are:`+array[i]);
    }
    
}