import './App.css';
import ChatBot from 'react-simple-chatbot';
import ApiMessage from './ApiMessage';
// import ThemeProvider from 'react-theme-provider';
import { ThemeProvider } from 'styled-components'

const theme = {
  background: '#f5f8fb',
  headerBgColor: '#B61942',
  headerFontColor: '#fff',
  headerFontSize: '15px',
  botBubbleColor: '#D1273F',
  botFontColor: '#fff',
  userBubbleColor: '#fff',
  userFontColor: '#4a4a4a',
};


function App() {
  return (
    <div className="App">
    <div className="Title">
      <h1>Chatbot weather forecast</h1>
    </div>
    <div className="Chatbot">
      <ThemeProvider theme={theme}>
        <ChatBot 
            steps={[
              {
                id: '1',
                message: 'Hi, I\'m Weatherbot! What can I do for you?',
                trigger: 'dynamicallyReachedStep',
              },
              {
                id: 'dynamicallyReachedStep',
                user: true, // réponse de l'utilisateur
                trigger: '3',
              },
              {
                id: '3',
                component: <ApiMessage/>, // dans le composant une passe à l'étape 2 pour redonner la main à l'utilisateur après que l'api est renvoyé un message
                waitAction: true, // Attendre que l'action précédente soit terminée
                asMessage: true, // Format de la réponse css
              }
            ]}
        />
      </ThemeProvider>
    </div>
    </div>
  );
}

export default App;
