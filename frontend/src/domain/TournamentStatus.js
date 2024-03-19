export const stateToString = (code) => {
    console.log(code)
    switch (code) {
        case 0:
            return "Fermé";
        case 1:
            return "Ouvert";
        case 2:
            return "En cours";
        case 2:
            return "Terminé";
        default:
            return "Status du tournoi";
    }

}