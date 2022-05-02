from charm.toolbox.pairinggroup import PairingGroup,ZR,G1,G2,GT,pair
def main():
 group = PairingGroup('SS1024')
 #This code can be used in order to measure the average execution time of cryptographic operations.
 #SS1024 makes symmetric pairing but other curves with asymmetric pairings are also allowed.
 n=1000
 Z={}
 Z1={}
 Z11={}
 g={}
 g1={}
 g11={}
 g111={}
 h={}
 h1={}
 h11={}
 h111={}
 E={}
 E1={}
 E11={}
 E111={}
 for k in range(n):
     Z[k]=group.random(ZR)
     Z1[k]=group.random(ZR)
     g[k] = group.random(G1)
     h[k] = group.random(G2)
     E[k]= group.random(GT) 
     
 t=0;
 for i in range(n):
     group.InitBenchmark( )
     group.StartBenchmark(["RealTime"])
     Z11[i]= Z1[i]*Z[i]
     group.EndBenchmark()
     t= t + group.GetBenchmark("RealTime")  
 print("Multiplication Time in Zp = ", t*1000/n,"ms") 
 print("* * * * * * * * * * * * * * * * * * * * * * * * * *")

 t=0;
 for i in range(n):
     group.InitBenchmark( )
     group.StartBenchmark(["RealTime"])
     g1[i]=g[i]**Z[i]
     group.EndBenchmark()
     t= t + group.GetBenchmark("RealTime")
 print("Exponentiation Time in G1 = ", t*1000/n,"ms") 
 
 t=0;
 for i in range(n):
     group.InitBenchmark( )
     group.StartBenchmark(["RealTime"])
     h1[i]=h[i]**Z[i]
     group.EndBenchmark()
     t= t + group.GetBenchmark("RealTime")  
 print("Exponentiation Time in G2 = ", t*1000/n,"ms") 
 
 t=0;
 for i in range(n):
     group.InitBenchmark( )
     group.StartBenchmark(["RealTime"])
     E1[i]=E[i]**Z[i]
     group.EndBenchmark()
     t= t + group.GetBenchmark("RealTime")
 print("Exponentiation Time in GT = ", t*1000/n,"ms") 
 print("* * * * * * * * * * * * * * * * * * * * * * * * * *")
   
 t=0;
 for i in range(n):
     group.InitBenchmark( )
     group.StartBenchmark(["RealTime"])
     g11[i]=g[i]*g1[i]
     group.EndBenchmark()
     t= t + group.GetBenchmark("RealTime")  
 print("Multiplication Time in G1 = ", t*1000/n,"ms") 
 
 t=0;
 for i in range(n):
     group.InitBenchmark( )
     group.StartBenchmark(["RealTime"])
     h11[i]=h[i]*h1[i]
     group.EndBenchmark()
     t= t + group.GetBenchmark("RealTime")  
 print("Multiplication Time in G2 = ", t*1000/n,"ms")  
 
 t=0;
 for i in range(n):
     group.InitBenchmark( )
     group.StartBenchmark(["RealTime"])
     E11[i]=E[i]*E1[i]
     group.EndBenchmark()
     t= t + group.GetBenchmark("RealTime")  
 print("Multiplication Time in GT = ", t*1000/n,"ms")
 print("* * * * * * * * * * * * * * * * * * * * * * * * * *")  
 t=0;
 
 for i in range(n):
     group.InitBenchmark( )
     group.StartBenchmark(["RealTime"])
     g111[i]=g[i]**(-1)
     group.EndBenchmark()
     t= t + group.GetBenchmark("RealTime")  
 print("Inverse Operation Time in G1 = ", t*1000/n,"ms") 
 t=0;
 for i in range(n):
     group.InitBenchmark( )
     group.StartBenchmark(["RealTime"])
     h111[i]=h[i]**(-1)
     group.EndBenchmark()
     t= t + group.GetBenchmark("RealTime")  
 print("Inverse Operation Time in G2 = ", t*1000/n,"ms") 
 
 t=0;
 for i in range(n):
     group.InitBenchmark( )
     group.StartBenchmark(["RealTime"])
     E111[i]=E[i]**(-1)
     group.EndBenchmark()
     t= t + group.GetBenchmark("RealTime")  
 print("Inverse Operation Time in GT = ", t*1000/n,"ms") 
 print("* * * * * * * * * * * * * * * * * * * * * * * * * *")
 
 t=0;
 for i in range(n):
     group.InitBenchmark( )
     group.StartBenchmark(["RealTime"])
     E111[i]=pair(g[i],h[i])
     group.EndBenchmark()
     t= t + group.GetBenchmark("RealTime")
 print("Pairing Time = ", t*1000/n,"ms")  
 
if __name__ == "__main__":
    main()
