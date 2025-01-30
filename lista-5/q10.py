# 10. sabendo-se que somente os municípios que possuem mais de 20 mil eleitores
# aptos tem segundo turno nas eleições para prefeito caso o primeiro colocado
# não tenha mais do que 50% DOS VOTOS. FAZER UM PROGRAMA QUE LEIA O NOME do município, a
# quantidade de eleitores aptos, o número de votos do candidato mais votado e informar se ele terá ou não
# segundo turno.

municipalityName = input("> Name of the municipality: ")
eligibleVoters = int(input("> Number of eligible voters: "))
mostVotedVotes = int(input("> Number of votes of the candidate with the most votes: "))

if mostVotedVotes == eligibleVoters * 0.50:
    print("> The most votaded candidate will have a Second Turn.")
else:
    print("> The most votaded candidate won't have a Second Turn.")
