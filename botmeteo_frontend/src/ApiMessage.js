import React, { useEffect, useState } from 'react'
import { Loading } from 'react-simple-chatbot';
import axios from 'axios';

// Création d'un composant
// Props c'est le même concept que les paramètres d'une classe mais pour un composant react
// On utilise la dependance react simple chatbot, quand on ajoute un nouveau composant dans le chatbot des props se créent par défault 
// comme par exemple previousStep

function ApiMessage(props) {
  // Création de 2 constantes Loading (pour le chargement de la réponse) et result pour stocker le résultat de mon api
  const [loading, setloading] = useState(true);
  const [result, setresult] = useState('');

  useEffect(() => {
    console.log(props); // On affiche dans la console les props du composant (pour connaitre le chemin pour afficher le message de l'utilisateur)
    //Call à ton api avec axios, je lui envoie la saisit de l'utilisateur
    axios.post('http://localhost:5000/messages', {
      message: props.previousStep.value,
      user: ''
    }) // si la requête fonctionne alors l'api renvoit une réponse
      .then(function (response) {
        console.log(response); // On affiche dans la console la réponse du serveur (pour avoir le chemin du message de réponse)
        //Ajouter la réponse dans le result
        setresult(response.data.message)
        setloading(false); // On désactive le loading car le serveur nous a renvoyé une réponse
        // On redonne la main à l'utilisateur en le renvoyant à l'étape 2 du chatbot pour qu'il puisse resaisir une requête
        props.triggerNextStep({ trigger: 'dynamicallyReachedStep' }) 
      }) // Si il y a une erreur dans la requête le serveyr r'envoit un message d'erreur
      .catch(function (error) {
        console.log(error);
        setresult('Sorry, I have a blackout :/');
        setloading(false);
        props.triggerNextStep({ trigger: 'dynamicallyReachedStep' })
      });
  }, [])

  return (
    <div>
      <div>
        {/* si loading true alors composant loading */}
        {loading && <Loading />}
        {/* si loading false alors balise span avec result */}
        {!loading &&
          <div>
            <span>{result}</span>
          </div>
        }
      </div>
    </div>
  )
}

export default ApiMessage


