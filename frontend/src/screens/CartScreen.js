import React, {useEffect} from 'react'
import { Link } from 'react-router-dom'
import { Row, Col, ListGroup, Image, Form, Button, Card } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'
import Message from '../components/Message'
import {addToCart} from '../actions/cartActions'

function CartScreen({match, location, history}) {
    const productId= match.params.id
    const qty = location.search

    console.log('qty:', qty)


    return (
        <div>
            Cart
        </div>
    )
}

export default CartScreen
