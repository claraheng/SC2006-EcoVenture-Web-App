// import React, { useState } from 'react';
// import axios from 'axios';

// function CreateAccountForm() {
//   const [username, setUsername] = useState('');
//   const [password1, setPassword1] = useState('');
//   const [password2, setPassword2] = useState('');


//   const handleSubmit = (event) => {
//     event.preventDefault();

//     const data = {
//         username,
//         password1,
//         password2,
//     };

//     axios.post('/createAccount', data)
//       .then(response => {
//         if (response.data.message === 'Success!') {
//             window.location.href = '/App';
//         }
//       })
//       .catch(error => {
//         console.log(error);
//       });
//   };


//   return (
//     <div className='container'>
//         <h1>Create Account</h1>

//       <form onSubmit={handleSubmit}>
//         <label>
//           <input type="text" value={username} onChange={e => setUsername(e.target.value)}
//             placeholder = "Username" />
//         </label>
//         <br />
//         <label>
//           <input type="password" value={password1} onChange={e => setPassword1(e.target.value)}
//             placeholder = "Password" />
//         </label>
//         <br />
//         <label>
//             <input type="password" value={password2} onChange={e => setPassword2(e.target.value)}
//             placeholder="Verify Password" />
//         </label>
//         <br />
//         <button type="submit">Create Account</button>
//       </form>
//     </div>
//   );
// }

// export default CreateAccountForm;