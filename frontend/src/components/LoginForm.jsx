// import React, { useState } from 'react';
// import axios from 'axios';

// function LoginForm() {
//   const [username, setUsername] = useState('');
//   const [password, setPassword] = useState('');

//   const handleSubmit = (event) => {
//     event.preventDefault();
//     axios.post('http://localhost:5000/login', { username, password })
//       .then(response => {
//         if (response.data.message === 'Welcome!') {
//           window.location.href = '/HomePage';
//         }
//         if (response.data.message === 'Logged in successfully') {
//           window.location.href = '/HomePage';
//         }
//       })
//       .catch(error => {
//         console.log(error);
//       });
//   };


//   return (
//     <div className='container'>
//     <h1>
//       Hello {username}
//     </h1>
//       <form onSubmit={handleSubmit}>
//         <div>
//           <input
//             type="text"
//             value={username}
//             onChange={e => setUsername(e.target.value)}
//             placeholder = "Username" />
//         </div>
//         <div>
//           <input
//             type="password"
//             value={password}
//             onChange={e => setPassword(e.target.value)}
//             placeholder = "Password" />
//         </div>
//         <button type="submit">Log In</button>
//     </form>
//     </div>
//   );
// }

// export default LoginForm;
