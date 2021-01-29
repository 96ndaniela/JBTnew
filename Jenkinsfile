pipeline { // pipe
    agent any   
    stages { //stage
	stage('validate - 1')
  { // first
	    steps { // fs
         script {
         sh 'chmod +x initial.sh' 
         sh './initial.sh'
         }
         
        } //fs
        } // first

	stage('#2') { // second
            steps { // ss
        python validation.py
            } // ss
        } // second

 
 
 


    } // stages
} // pipe
