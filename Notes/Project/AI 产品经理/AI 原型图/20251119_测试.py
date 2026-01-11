
def calBMI(Weight,height):
    BMI = Weight /(height**2)
    return BMI


static func calcCtlAtl(trimp: Double) ->(ctl:Double, atl:Double){
    // CTL(Fitness) = CTLy + (Trimp-CTLy)/42
    // ATL(Fatigue) = ATLy + (Trimp-ATLy)/7
    (trimp/CTL_DAYS, trimp/ATL_DAYS)
}

