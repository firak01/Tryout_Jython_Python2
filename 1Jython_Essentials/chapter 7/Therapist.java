public class Therapist {

    public MentalState analyze(MentalState mental) {
        System.out.println("mental state? "+mental.askEnergy());
        return mental;
    }

}

/*
Test with the following at the Jython Prompt

>>> from flexibleMind import FlexibleMentalState
>>> mental = FlexibleMentalState()
>>> mental.energy = -1
>>> import Therapist
>>> therapist = Therapist()
>>> mental2 = therapist.analyze(mental)
mental state? -1
>>> mental2.energy
-1
>>> mental2 is mental
1  

*/
