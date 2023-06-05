
// Should NOT generate warning
int main(){
//    float x = 0.5;
//    int y = (int)x;
    int z = (int)0.5;
    while(z < 3){
        ++z;
        printf("%d\n", z);
    }
//    return 1;
}
