import React, { useState, useEffect } from 'react';
import axios from 'axios';

//PRE: product is an object with the following structure:
//POST: the product is updated in the database
export const getProducts = () => {
  const [products, setProducts] = useState([]);
  useEffect(() => {
    axios.get('/products').then((response) => {
      if (Array.isArray(response.data)) {
        setProducts(response.data);
      } else {
        console.error('Error: products is not an array');
      }
    });
  }, []);
  return products;
};

//PRE: product is an object with the following structure:
//POST: the product is added to the database
export const postProduct = () => {
  return (product) => {
    return axios.post('/products', product);
  };
}

//PRE: productId is a string with the id of the product to be deleted
//POST: the product is deleted from the database
export const deleteProduct = () => {
  return (productId) => {
    return axios.delete(`/products/${productId}`);
  };
}

//PRE: user is an object with the following structure:
//POST: the user is updated in the database
export const getUsers = () => {
  const [users, setUsers] = useState([]);
  useEffect(() => {
    axios.get('/users').then((response) => {
      if (Array.isArray(response.data)) {
        setUsers(response.data);
      } else {
        console.error('Error: users is not an array');
      }
    });
  }, []);
  return users;
};

//PRE: user is an object with the following structure:
//POST: the user is added to the database
export const postUser = () => {
  return (user) => {
    console.log(user);
    return axios.post('/users', user);
  };
}

//PRE: userId is a string with the id of the user to be deleted
//POST: the user is deleted from the database
export const deleteUser = () => {
  return (userId) => {
    return axios.delete(`/users/${userId}`);
  };
}       

//PRE: product is an object with the following structure:
//POST: the product is updated in the database
export const getProductsBought = () => {
  const [productsBought, setProductsBought] = useState([]);
  useEffect(() => {
    axios.get('/productsBought').then((response) => {
      if (Array.isArray(response.data)) {
        setProductsBought(response.data);
      } else {
        console.error('Error: productsBought is not an array');
      }
    });
  }, []);
  return productsBought;
};
//PRE: productBought is an object with the following structure:
//POST: the productBought is added to the database
export const postProductBought = () => {
  return (productBought) => {
    return axios.post('/productsBought', productBought);
  };
}

//PRE: productBoughtId is a string with the id of the productBought to be deleted
//POST: the productBought is deleted from the database
export const deleteProductBought = () => {
  return (productBoughtId) => {
    return axios.delete(`/productsBought/${productBoughtId}`);
  };
}
