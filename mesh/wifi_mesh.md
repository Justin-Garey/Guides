# Wi-Fi Mesh

Better Approach to Mobile Ad-hoc Networking IV (B.A.T.M.A.N.-adv) allows you to take control of the Wi-Fi chip or card on a device to be used in an ad-hoc mesh network. 

As an example, setting this up on a group of Raspberry Pis would create a private mesh network that could be connected to the greater Internet but is not necessary for communication between devices within the mesh. 

This [guide](https://meshunderground.com/posts/raspberry-pi-mesh-network-guide-build-a-resilient-wireless-network) on meshunderground.com for setting up on a Raspberry Pi proved very effective. To note while setting up, set the MTU to 1480 so packets are not fragmented with the extra space taken by B.A.T.M.A.N-adv.

## Resources

- [Documentation](https://www.open-mesh.org/projects/open-mesh/wiki) on open-mesh.org.
- [Wikipedia](https://en.wikipedia.org/wiki/B.A.T.M.A.N.) entry.
- [Guide](https://meshunderground.com/posts/raspberry-pi-mesh-network-guide-build-a-resilient-wireless-network) on meshunderground.com for setting up on a Raspberry Pis.